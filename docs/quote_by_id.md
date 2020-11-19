# Get Quote by id

| **Name of Series** |
| ------------------ |
| breakingbad        |
| dark               |
| moneyheist         |
| gameofthrones      |

</br>

**URL** : `https://web-series-quotes.herokuapp.com/{series_name}/{quote_id}`

## Example
  
**Method** : `GET`

**URL** : ```https://web-series-quotes.herokuapp.com/moneyheist/34```

**Auth required** : `False`

**Code** : `200 OK`

```json
{
  "author": "Berlin",
  "id": 24,
  "quote": "For a joke to work, it has to have part of truth and part of pain."
}
```
