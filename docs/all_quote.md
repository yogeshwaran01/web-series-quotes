# Get all quotes

| **Name of Series** |
| ------------------ |
| breakingbad        |
| dark               |
| moneyheist         |
| gameofthrones      |

</br>

**URL** : `https://web-series-quotes.herokuapp.com/{series_name}`

## Example
  
**Method** : `GET`

**URL** : ```https://web-series-quotes.herokuapp.com/breakingbad```

**Auth required** : `False`

**Code** : `200 OK`

```json
[
    {
         "author": "Walter White",
         "id": 1,
         "quote": "I am not in danger, Skyler. I AM the danger!"
   },
    ...
]
```
