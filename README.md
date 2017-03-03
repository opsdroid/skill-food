# opsdroid skill food

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to suggest tasty food.

## Requirements

An API key from [Food2Fork](http://food2fork.com/about/api).

## Configuration

```yaml
skills:
  - name: food
    api-key: "myapikeyfromfood2fork"  # Required
```

## Usage

#### `What shall I eat?`

Suggests some food from Food2Fork.

> user: What shall I eat?
>
> opsdroid: How about chicken fajitas?
>
> opsdroid: http://example.com/link-to-recipe-image.jpg

## License

GNU General Public License Version 3 (GPLv3)
