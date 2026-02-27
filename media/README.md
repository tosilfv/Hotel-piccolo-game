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
- `music_yard.wav` - Music for yard scene
- `sound_jump.wav` - Sound effect for yard scene

### `graphics/`

Contains all visual assets organized by category:

#### `hotel/`

Background images for different hotel scenes:
- `entrance_normal.png` - Sky surface for entrance scene
- `outdoor_ground_normal.png` - Ground surface for outdoor scenes
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
