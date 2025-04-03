import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define CUBE vertices and edges
CUBE_VERTICES = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
)

CUBE_EDGES = (
    (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
    (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
)

# Define CUBE faces (question 5)
CUBE_FACES = (
    (0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4),
    (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6)
)

# Define PYRAMID vertices and edges
PYRAMID_VERTICES = (
  (1, -1, 1), (-1, -1, 1), (0, -1, -1), (1, 1, 0.5)
)

PYRAMID_EDGES = (
  (0,1), (0,2), (0,3), (2,1), (2,3), (3,1)
)

# Define PYRAMID faces (question 5)
PYRAMID_FACES = (
  (0, 1, 2), (0, 1, 3), (0, 2, 3),
  (1, 2, 3) 
)

# Define PRISM vertices and edges
PRISM_VERTICES = (
  (-1, -1, 1), (1, -1, 1), (0, 1, 1), 
  (-1, -1, -1), (1, -1, -1), (0, 1, -1),
)
PRISM_EDGES = (
  (0,1), (0,2), (1,2), 
  (3,4), (3,5), (4,5), 
  (0,3), (1,4), (2,5),
)

# Define PRISM faces (question 5)
PRISM_FACES = (
    (0, 1, 2), (3, 4, 5), (0, 1, 4, 3),
    (1, 2, 5, 4), (2, 0, 3, 5)
)

# Define the shapes with their vertices and edges
# and faces (question 5)
SHAPES = [
    (CUBE_VERTICES, CUBE_EDGES, CUBE_FACES),
    (PYRAMID_VERTICES, PYRAMID_EDGES, PYRAMID_FACES),
    (PRISM_VERTICES, PRISM_EDGES, PRISM_FACES)
]

# Define the colors for each face (question 5)
COLOURS = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),  # Red, Green, Blue
    (1, 1, 0), (1, 0, 1), (0, 1, 1)   # Yellow, Magenta, Cyan
]

def draw_shape(vertices, edges, faces, scale):
    """Draws a shape using OpenGL."""
    glEnable(GL_DEPTH_TEST)

    # Draw faces with colors (question 5)
    for i, face in enumerate(faces):
        if len(face) == 3:  # If the face is a triangle
            glBegin(GL_TRIANGLES)
        else:  
            glBegin(GL_QUADS)

        glColor3fv(COLOURS[i % len(COLOURS)]) # Assign colour to each face (Question 5)
        for vertex in face:
            scaled_vertex = (
                vertices[vertex][0] * scale[0],
                vertices[vertex][1] * scale[1],
                vertices[vertex][2] * scale[2]
            )
            glVertex3fv(scaled_vertex)
        glEnd()

    glColor3fv((1, 1, 1))  # Draw white edges
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:               # Question 4: Scale the vertices
            scaled_vertex = (
                vertices[vertex][0] * scale[0],
                vertices[vertex][1] * scale[1],
                vertices[vertex][2] * scale[2]
            )
            glVertex3fv(scaled_vertex)
    glEnd()


def main():
    """Main function to initialize pygame and OpenGL, and render the rotating cube."""
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, display[0] / display[1], 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    current_shape = 0   # Index of the current shape
    translation = [0, 0, 0]   # Translation values for x, y, z(question 2)
    rotation = [0, 0, 0] # Rotation values for x, y, z (question 3)
    continuous_rotation = True  # Flag for continuous rotation (question 3)
    scale = [1, 1, 1]  # Scale values for x, y, z (question 4)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE: # Switch to next shape
                    current_shape = (current_shape + 1) % len(SHAPES)

                # QUESTION 2: Add translation controls
                elif event.key == K_a:      # Move left (negative x)
                    translation[0] -= 0.2 
                elif event.key == K_d:      # Move right (positive x)
                    translation[0] += 0.2  
                elif event.key == K_w:      # Move up (postive y)
                    translation[1] += 0.2  
                elif event.key == K_s:      # Move down (negative y)
                    translation[1] -= 0.2  
                elif event.key == K_q:      # Move forward (negative z)
                    translation[2] -= 0.2  
                elif event.key == K_e:      # Move backward (positive z)
                    translation[2] += 0.2  

                # QUESTION 3: Add rotation controls
                elif event.key == K_i:      # Rotate positively around x-axis
                    rotation[0] += 5
                elif event.key == K_k:      # Rotate negatively around x-axis
                    rotation[0] -= 5
                elif event.key == K_j:      # Rotate positively around y-axis
                    rotation[1] += 5
                elif event.key == K_l:      # Rotate negatively around y-axis
                    rotation[1] -= 5
                elif event.key == K_u:      # Rotate positively around z-axis
                    rotation[2] += 5
                elif event.key == K_o:      # Rotate negatively around z-axis
                    rotation[2] -= 5
                elif event.key == K_r:  # Toggle continuous rotation
                    continuous_rotation = not continuous_rotation

                # QUESTION 4: Add scaling controls
                elif event.key == K_z:     # Increase X scale
                    scale[0] *= 1.1
                elif event.key == K_x:     # Decrease X scale
                    scale[0] *= 0.9
                elif event.key == K_c:     # Increase Y scale 
                    scale[1] *= 1.1
                elif event.key == K_v:     # Decrease Y scale
                    scale[1] *= 0.9       
                elif event.key == K_b:     # Increase Z scale
                    scale[2] *= 1.1
                elif event.key == K_n:     # Decrease Z scale
                    scale[2] *= 0.9

        if continuous_rotation:            # Question 3: Continuous rotation
          rotation[0] += 0.5  # Slow rotation around X-axis
          rotation[1] += 0.5  # Slow rotation around Y-axis
          rotation[2] += 0.5  # Slow rotation around Z-axis

        glLoadIdentity()
        gluPerspective(45, display[0] / display[1], 0.1, 50.0)
        glTranslatef(translation[0], translation[1], translation[2] - 5)  # Apply translation (question 2)
        
        # Apply rotation (question 3)
        glRotatef(rotation[0], 1, 0, 0)  # Apply rotation around x-axis
        glRotatef(rotation[1], 0, 1, 0)  # Apply rotation around y-axis
        glRotatef(rotation[2], 0, 0, 1)  # Apply rotation around z-axis
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_shape(*SHAPES[current_shape], scale)
        pygame.display.flip()
        pygame.time.delay(10)

    pygame.quit()

if __name__ == "__main__":
    main()
