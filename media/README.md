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
- `music_hotel.wav` - Music for indoor scenes
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
- `ballroom.png` - Sky surface for ballroom scene
- `bar.png` - Sky surface for bar scene
- `concierge.png` - Sky surface for concierge scene
- `corridor_club.png` - Sky surface for corridor club scene
- `corridor_deluxe.png` - Sky surface for corridor deluxe scene
- `corridor_empty.png` - Sky surface for empty corridor scene
- `corridor_staff.png` - Sky surface for corridor staff scene
- `corridor_standard.png` - Sky surface for corridor standard scene
- `corridor_suite.png` - Sky surface for suite scene
- `elevator.png` - Sky surface for elevator scene
- `entrance.png` - Sky surface for entrance scene
- `garage.png` - Sky surface for garage scene
- `indoor_ground.png` - Ground surface for indoor scenes
- `inside_garage.png` - Sky surface for inside garage scene
- `inside_luggage.png` - Sky surface for inside luggage scene
- `inside_staff.png` - Sky surface for inside staff scene
- `luggage.png` - Sky surface for luggage scene
- `luxusrestaurant.png` - Sky surface for luxusrestaurant scene
- `outdoor_ground.png` - Ground surface for outdoor scenes
- `reception.png` - Sky surface for reception scene
- `restaurant.png` - Sky surface for restaurant scene
- `sauna.png` - Sky surface for sauna scene
- `services.png` - Sky surface for services scene
- `sofas.png` - Sky surface for sofas scene
- `yard.png` - Sky surface for yard scene

#### `items/`

Item images for different actions
- `bag.png` - Bag
- `bill.png` - Bill
- `carkeys.png` - Car keys
- `coin.png` - Coin
- `pillow.png` - Pillow
- `trash1.png` - Trash version 1
- `trash2.png` - Trash version 2
- `trolley.png` - Trolley

#### `player/`

Player character sprites for different states and directions:
- `piccolo_left_run1.png` - Running frame 1 (left-facing)
- `piccolo_left_run2.png` - Running frame 2 (left-facing)
- `piccolo_left_stand.png` - Standing (left-facing)
- `piccolo_run1.png` - Running frame 1 (right-facing)
- `piccolo_run2.png` - Running frame 2 (right-facing)
- `piccolo_stand.png` - Standing (right-facing)
