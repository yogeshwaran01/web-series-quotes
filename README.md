![web-series-quotes-title](web-series-quotes-title.png)

# Web-Series-Quotes-Api

Api for Quotes of various web-series. Api automatically generate quotes with background image. Api also returns the Quotes and its author as json.

## Available Web-Series

- [Breaking Bad](https://web-series-quotes.herokuapp.com/breakingbad)
- [Dark](https://web-series-quotes.herokuapp.com/dark)
- [Game Of Thrones](https://web-series-quotes.herokuapp.com/gameofthrones)
- [Money Heist](https://web-series-quotes.herokuapp.com/moneyheist)

## URI

```url
https://web-series-quotes.herokuapp.com
```

## Generating Quotes with images

There are four method to Generate Quotes

- Generating Quotes with in-build images
- Generating Quotes with in your own images
- Generating Quotes with blank colored Backgroud
- Generating Quaotes of your own quote and own image

### Generating Quotes with in-build images

Presently there is four images are in build
| **Name of images** |
| ------------------ |
| breakingbad        |
| dark               |
| moneyheist         |
| gameofthrones      |

```url
/generate/{series_name}/{quote_id}/image?src={name_of_image}&size={font_size}&color={font_color}
```

#### Example

```url
https://web-series-quotes.herokuapp.com/generate/breakingbad/1/image?src=breakingbad&size=150&color=pink
```

![image](https://web-series-quotes.herokuapp.com/generate/breakingbad/1/image?src=breakingbad&size=150&color=pink)

### Generating Quotes with in your own images

```url
/generate/{series_name}/{quote_id}/image?src={url_of_your_image}&color={font_color}&size={font_size}
```

#### Example

```url
https://web-series-quotes.herokuapp.com/generate/moneyheist/5/image?src=https://www.gstatic.com/webp/gallery/3.png&color=yellow&size=100
```

![image](https://web-series-quotes.herokuapp.com/generate/moneyheist/5/image?src=https://www.gstatic.com/webp/gallery/3.png&color=yellow&size=100)

### Generating Quotes with blank colored Backgroud

```url
/generate/{series_name}/{quote_id}/blank?fore={foreground}&back={background}&size={font_size}
```

#### Example

```url
https://web-series-quotes.herokuapp.com/generate/breakingbad/10/blank?fore=red&back=yellow&size=300
```

![image](https://web-series-quotes.herokuapp.com/generate/breakingbad/10/blank?fore=black&back=yellow&size=300)

### Generating Quote of your own quote and image

```url
/generate/image?src={url_of_image}&color={font_color}&size={font_size}&text={your_text}
```

#### Example

```url
https://web-series-quotes.herokuapp.com/generate/image?src=https://www.gstatic.com/webp/gallery/1.png&color=yellow&size=100&text=Hello+world
```

```url
https://web-series-quotes.herokuapp.com/generate/blank?text=Hello+I'am+Python
```

![image](https://web-series-quotes.herokuapp.com/generate/image?src=https://www.gstatic.com/webp/gallery/1.png&color=yellow&size=100&text=Hello%20world)


## API

### All Quotes

```url
/breakingbad
```

```url
/dark/
```

```url
/gameofthrones
```

```url
/moneyheist/
```

### Random Quotes

```url
/random/breakingbad/
```

```url
/random/breakingbad/{number_of_quotes}
```

```url
/random/dark/
```

```url
/random/dark/10
```

```url
/random/gameofthrones/
```

```url
/random/moneyheist
```

### Quote Id

```url
/breakingbad/{id}/
```

```url
/dark/23
```

```url
/gameofthrones/{id}
```

```url
/moneyheist/4/
```

### Contributing

- Add other your favourite webseries quotes in ```data``` folder
- Add route path in ```routes.py```
- Make PR
