# Media Assets

This directory contains all media assets used in the Piccolo game.

**Naming Convention:**
- `*_normal.png` - Standard resolution images
- `*_large.png` - Higher resolution images (for indoor scenes)
Large images are intended for higher-resolution or indoor scenes and may be
loaded dynamically in the future.

## Usage

All images are loaded using the `helpers.load_image()` function from
`utils/helpers.py`, which handles error cases by providing placeholder
surfaces if files are missing.

## License

See the `LICENCE` file in this directory for licensing information.

## Directory Structure

### `graphics/`
Contains all visual assets organized by category:

#### `hotel/`
Background images for different hotel scenes:
- `entrance_normal.png` - Sky surface for entrance scene
- `outdoor_ground_normal.png` - Ground surface for outdoor scenes
- `yard_normal.png` - Sky surface for yard scene

#### `player/`
Player character sprites for different states and directions:
- `piccolo_run1_normal.png` - Running frame 1 (right-facing)
- `piccolo_run2_normal.png` - Running frame 2 (right-facing)
- `piccolo_stand_normal.png` - Standing (right-facing)
