# Media Assets

This directory contains all media assets used in the Piccolo game.

**Naming Convention:**

- `*_normal.png` - Standard resolution images
- `*_large.png` - Higher resolution images (for indoor scenes)

## Usage

All images are loaded using the `helpers.load_image()` function from
`utils/helpers.py`, which handles error cases by providing placeholder
surfaces if files are missing.

## License

See the `LICENCE` file in this directory for licensing information.

## Directory Structure

### `audio/`

Contains all audio assets:
- `elevator.wav` - Sound effect for elevator scene
- `music_yard.wav` - Music for yard scene
- `sound_jump.wav` - Sound effect for yard scene
- `tip.wav` - Sound effect for tip

### `graphics/`

Contains all visual assets organized by category:

#### `font/`

Contains font file:
- `Pixeltype.ttf` - Pixel-style font used in the game

#### `hotel/`

Background images for different hotel scenes:
- `corridor_elevator_normal.png` - Sky surface for elevator scene
- `corridor_empty_normal.png` - Sky surface for empty corridor scene
- `corridor_rooms_normal.png` - Sky surface for rooms corridor scene
- `corridor_suite_normal.png` - Sky surface for suite scene
- `entrance_normal.png` - Sky surface for entrance scene
- `indoor_ground_normal.png` - Ground surface for indoor scenes
- `outdoor_ground_normal.png` - Ground surface for outdoor scenes
- `reception_normal.png` - Sky surface for reception scene
- `yard_normal.png` - Sky surface for yard scene

#### `items/`

Item images for different actions
- `bag_normal.png` - Bag (right-facing)
- `trolley_empty_normal.png` - Empty trolley (right-facing)

#### `player/`

Player character sprites for different states and directions:
- `piccolo_left_run1_normal.png` - Running frame 1 (left-facing)
- `piccolo_left_run2_normal.png` - Running frame 2 (left-facing)
- `piccolo_left_stand_normal.png` - Standing (left-facing)
- `piccolo_run1_normal.png` - Running frame 1 (right-facing)
- `piccolo_run2_normal.png` - Running frame 2 (right-facing)
- `piccolo_stand_normal.png` - Standing (right-facing)
