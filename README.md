# 3D Shape Visualizer

This projet is a 3D shape renderer that allows users to manipulate basic 3D models (Cube, Pyramid, and Prism) with different transformations like translation, rotation, scaling, and coloring. The shapes have colorful faces with white edges.

## Features

- **Shape Switching**: Switch between Cube, Pyramid, and Prism with the `SPACE` key.
- **Translation**: Move the model along all 3 axes (X, Y, Z) using the `WASD` and `QE` keys.
- **Rotation**: Rotate the model in local space along all 3 axes using the `IJKLUO` keys.
- **Continuous Rotation**: Press the `R` key to stop/start continuous rotation.
- **Scaling**: Scale the model along the X, Y, and Z axes using the `Z/X`, `C/V`, and `B/N` keys.
- **Coloring**: Each face of the shape is colored differently, while the edges are white.

## Prerequisites

To run this project, you need to have the following installed:

- Python 3.x
- Pygame (for window and event handling)
- PyOpenGL (for 3D rendering)

You can install the required libraries by running:

```
pip install pygame PyOpenGL
```

## How to Run

1. Clone or download this repository.
2. Ensure you have Python 3.x installed.
3. Install the required dependencies using the command mentioned above.
4. Run the main Python script:

```
python q1_display.py
```

## Key Controls

- **Switch Shape**: `SPACE`
- **Translate Shape**:
  - `W`: Move up along the Y-axis
  - `S`: Move down along the Y-axis
  - `A`: Move left along the X-axis
  - `D`: Move right along the X-axis
  - `Q`: Move forward along the Z-axis
  - `E`: Move backward along the Z-axis
- **Rotate Shape**:
  - `I`: Rotate up along the X-axis
  - `K`: Rotate down along the X-axis
  - `J`: Rotate left along the Y-axis
  - `L`: Rotate right along the Y-axis
  - `U`: Rotate clockwise along the Z-axis
  - `O`: Rotate counterclockwise along the Z-axis
- **Continuous Rotation**: Hold `R`
- **Scale Shape**:
  - `Z`: Scale up along the X-axis
  - `X`: Scale down along the X-axis
  - `C`: Scale up along the Y-axis
  - `V`: Scale down along the Y-axis
  - `B`: Scale up along the Z-axis
  - `N`: Scale down along the Z-axis

## How It Works

### Rendering:
The program uses **OpenGL** for 3D rendering. It supports wireframe-style rendering, where the **edges** of the models are drawn in **white**, while each **face** of the model is assigned a unique color.

### Transformations:
- **Translation**: Changes the position of the model in the 3D space.
- **Rotation**: Rotates the model along its local axes.
- **Scaling**: Resizes the model along each axis, allowing stretching or squeezing.
  
### Shape Types:
- **Cube**: A 3D cube with 6 colored faces and 12 white edges.
- **Pyramid**: A pyramid with 4 triangular faces and 1 square base.
- **Prism**: A triangular prism with 5 faces and 9 edges.
