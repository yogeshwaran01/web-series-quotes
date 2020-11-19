# Get Random Quote

| **Name of Series** |
| ------------------ |
| breakingbad        |
| dark               |
| moneyheist         |
| gameofthrones      |

</br>

**URL** : `https://web-series-quotes.herokuapp.com/random/{series_name}`

**URL** : `https://web-series-quotes.herokuapp.com/random/{series_name}/{number_of_random_quotes}`

## Example
  
**Method** : `GET`

**URL** : ```https://web-series-quotes.herokuapp.com/random/dark/2```

**Auth required** : `False`

**Code** : `200 OK`

```json
[
  {
    "author": "Mikkel Nielsen",
    "id": 1,
    "quote": "There is no such thing as magic, just illusion. Things only change when we change them. But you have to do it skillfully, in secret. Then it seems like magic."
  },
  {
    "author": "The Stranger",
    "id": 10,
    "quote": "Yesterday, today and tomorrow are not consecutive, they are connected in a never-ending circle. Everything is connected"
  }
]
```
