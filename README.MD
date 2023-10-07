# AstronomicalDistanceConverterAPI

Astronomical unit converter API built with FastAPI.🌌

### [Demo Video 📺](https://youtu.be/-jrgWP_N6xk)


## Requirements 📦

- FastAPI
- Uvicorn

## Installation ⬇️

download source code from Github 💾
`git clone https://github.com/DogukanUrker/AstronomicalDistanceConverterAPI.git`

go to directory 📁
`cd AstronomicalDistanceConverterAPI`

install requirements.txt 🔽
`pip install -r requirements.txt`

it's ready to run 🎉
`python main.py`

## Requests 📚

Transtale X to Y

```
/x/y/{int}
```
X and Y can be:
- astronomical-unit / au
- kilometer / km
- light-minute / lm
- light-second / ls
- light-year / ly
- miles / mi
- parsec / pc
 
Note:
If X value is abbreviation then Y value must be abbreviated to, same for full unit names.

Examples:

```
/ly/km/3
```

```
28382191417742.402
```


```
/astronomical-unit/light-second/3
```

```
1497.01434
```


```
/parsec/mi/3
```

```json
{
    "detail": "Not Found"
}
```

### Contributors 💕

<a href="https://github.com/dogukanurker"><img src="https://avatars.githubusercontent.com/u/62756402" title="ngryman" width="80" height="80"></a>

### Support 💰

<a href="https://dogukanurker.com/donate" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-red.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
