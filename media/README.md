# Media Assets

This directory contains all media assets used in the Piccolo game.

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
- `sound_elevator.wav` - Sound effect for elevator scene
- `sound_jump.wav` - Sound effect for yard scene
- `sound_tip.wav` - Sound effect for tip

### `graphics/`

Contains all visual assets organized by category:

#### `font/`

Contains font file:
- `Pixeltype.ttf` - Pixel-style font used in the game

#### `hotel/`

Background images for different hotel scenes:
- `corridor_elevator.png` - Sky surface for elevator scene
- `corridor_empty.png` - Sky surface for empty corridor scene
- `corridor_rooms.png` - Sky surface for rooms corridor scene
- `corridor_suite.png` - Sky surface for suite scene
- `entrance.png` - Sky surface for entrance scene
- `indoor_ground.png` - Ground surface for indoor scenes
- `outdoor_ground.png` - Ground surface for outdoor scenes
- `reception.png` - Sky surface for reception scene
- `yard.png` - Sky surface for yard scene

#### `items/`

Item images for different actions
- `bag.png` - Bag
- `bill.png` - Bill
- `coin.png` - Coin
- `trolley.png` - Trolley

#### `player/`

Player character sprites for different states and directions:
- `piccolo_left_run1.png` - Running frame 1 (left-facing)
- `piccolo_left_run2.png` - Running frame 2 (left-facing)
- `piccolo_left_stand.png` - Standing (left-facing)
- `piccolo_run1.png` - Running frame 1 (right-facing)
- `piccolo_run2.png` - Running frame 2 (right-facing)
- `piccolo_stand.png` - Standing (right-facing)
