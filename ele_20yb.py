
"""
抢20
卡密变量 lqkm
账号变量 elmqqck
推送变量  lp , id
lp为 wxpusher 账号令牌
id为 wxpusher id


令牌和id获取方式
打开后台  
https://wxpusher.zjiecode.com/admin/main
应用管理-appToken 就是令牌 
主题管理-TopicId 就是id

 * cron: 55 55 9 * * *
内置定时 09:59:59
脚本定时 55 50 9 * * * 
默认一个账号抢劵次数20次 200毫秒
暂不支持修改

"""
const $ = new Env('饿了么20抢券异步版本--嘎嘎好使');
import lzma, base64
exec(lzma.decompress(base64.b64decode('/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4BulCspdADSbSme4Ujxz9PV7sB8UcIoUWuZs9sNkRf/1SgcKaWzYgR5aDpehK9tg771pjq1DB4u5hmBtb6P9XcNvmGU7fI7McDb7joxfbGElqqskFy0CCY2HjNniiSbjCzHe0tk77nx6dB8SHC4xKuPtja6rN7X2tBJHlZ0+Cnv3NgebzooreAvoAeT4+SCbwaf9L98IilSHYmh9oCUzNNB2FXz4tm99Aj1+E7wYsv2p/TDTeK62AgUfno7DA9L1py5H8Wv09q/xzxitEwoE6a+bNPHkhMJz2N/yk7gR/WCpp+JRVp+Fo7cM7HXUS3qg+Uc4WZ2bDGFXIjvOcb6QAqr+Zfmw6ZxnOZUpzI0y4SPSzYCnnBUKdOtF2sq9Aw9E2u+d8VftVk5cSKrPwg6MdkhT1w951xgo4qjj61Kgk1a39AVKMofX2kyxk421ONLjT6j60idko5mkj5Hsu5bHGSCvFe6pc6i435Vr8kM2mic3s7o+ula8oxAHDHYdd50eKVYUZhoPqOxRuIvIPWdbbldlA0qtq7JpQMOEvrYG7k/KXS7/4btSQW4Yfdil26qACUdOcfK+uK2ZuYQCuCp87dSSqP8OtwC/igKz1YrwRzV64JkIXy/ZVstf4DtKzMw6L9Snnfiu7gXyiz7VT53upGCx7LGqIL8mAtVQUjCbK55YFfZqtFer9hz/WlXOW/BynVgbCHpkBd/gC8h015YUmycUpW00mQzH8jaxy6ebawCZUrXQFdLraGI2jnacFdags1HFUs30D178ro8qI90OpGQePK+zp9Fl9UXinOewCgjTaq/xmKiFNklIwakz+uTUhEvrdqYDEWkDNcTmEelBDBbfl1SEHUs5zF68g8IpgoxkQdEBD1yxsnNh8Dw4BMSqIjR0MObMpwQDZ3N0GDekhv7TL3kgS/is0auHNRlNBSJfPW/4aBaSkx9ZN+IuBUlyaxoIioue+Y9+49t2UBf8qGI5qJafV76sP32KbInH9nvs6SL0+Kzu9JYWRXMaG7/u6gU9tcZmlCAnAEwcncWqDlIkA/79/ezxjI6lZF2A3qj7S1/su7xNz1ddg3iUNs89qumN0EbnvoCj0M9Equb+8ey6Vcv3L6QJKI+RVz/uKvh7Hb7bMjo41qgYflRyKcEK49XWQ4QVEL7tsYlfeMoUflwxVWhNYV6ouPbl0uJfYk6iCgRgIdOcL6HznWZk36Lw53RERr57FCNl83gDH/7BsnPq4QzQZW47w3W0ojSmNFVzNvJrlTx1wW3NCFn8ltml1PJe9IRYp30TaCh6Er1N3J0X16SlOu0E6gl34Brt8quce/EV96HTmHHZxUkT9jPpYLqGhp7LCCeu7VQGDtHQC+oGyYyVBUJfpelHCtPlEOuQ5XlcwbqJvLeVbIog+5zc76CiVh/u78yH4pDKdxNv/2fj5Eh/+coHMaIJZw7lRksngEbd4mB1ukncOO376wukMDB2xlzxG+BCH/b6N00sefFJAuqp7NdCwnKNQh9uZDCLmboZZ1VcOE4Pzy/zborsQBnS9q/04+E1C0IZWju3C7MqNNnWx+LqFgc2dpr+UbXeFK0M+s6cjHQqBA2tPW/AHc2cJOc5k5GXmjqVZPMMmO9iqx1e3oQtVVLQz0dr1dWkJatTMv0VZuQl/FiN0IB7jSQulmt01hPL45wqINidZGxWyHupoPp/68aSeYT9niR85e+wa5Ntg2TL+PqZrRzMwmC8zaHY/UMfD/cX+83jfowi90A9xG8VKFDJ0vBltsheRpjpVN85LZQgJhEj9WIOCcob428dZOzxxw341YLPlmo1KCDd9U52COd7xABXg+C0N7N/ehfmXwSDO2ILPhrI7bEZs7FJ9XEhfX587vIAI2Nlt22VPYNs2jI/+zZBcNE83RFoC7wEAFWCfYBySe4xh//9Dybk93JJoDaeug0o4YnJHiWQTybunwcMjK1orVbwXDfxqygXMlrIyxKt0vb2JtiTinUeYvURsHhFNfqcgDi1i7UKSvnucNBq/CcdEFkt3+j8pTPV7mjwGo9M9l1jidWt/yIwPiMBerNXS3/66y5CJCAOw5Fw85vUBaS6egDGW7tLMZdu51l5Rzq3sET/dwQoKORIvuVxo5C1xmYreEFgj/HdDjjuwJ9IwVKnXjAxFtPkeBtKs9yoZpkOIRbk7rMWdWfZfcC4H2uADJ6oc7ZyWkczhx9EEryj76e65YtH9EW4hcxKBAHVjSJGB/f8vgxQ7MX6NFnzJLsCD+t0EkpCLmjN28x9dHEPfZ+6Qg+AGdb7+KWUUqXJ6TpiRI5CvA1AKyLvc2YIfyUQ2Q8MFNWYw3/UiXmIB3YkxfnG+ItSoem3kUPnb6py5CiPVfI2LyRORwIhRHchWZSsvlSE8VZH/MTZ7eU/Gl7hPPdsdIOvOCEFd4zti2vrBVBqL1V+Uhb7kmfDHlhXTq/5+4EriC1nAbxUhRltNgpMTfQpeyGXXU2wzsvksJgHy5nWeM69GjoqjJGol/jgHRQg94V79T+hSv5JgCDruGSLOMFtT9DXEcbh2WuVh10+jFrG7jZXZUTW6HTmpQOKcFA3Mt5JbH4nN9xJd9PIE19EpLSU5nXi6u5YWDOPJmT4NKc0rSZXr5CIdoOrVnE2fUl5vyMjptJZJXd5zVFpBCsGwWNcRNKYdMCXWMn5UeWsUlGu2aXN1JEZ+S2AvZ7jv/MrPtj2WL+1k6EiB/00YPlIq1CQNDZ47mq84FpjuZaLxZqhH8LbzAjSvn8Qg9SQbZ9iz/Mb9kFSz7OIiTcWOyF+ejSxavwzPtIur/e/uUhpARW5nx6ot0DIlKaW7gH56Im3P9WZ3Wvd2cTq7vzQG3+zPE7s4q70SWHbZXnNFmBlwtMMmvfAOujs61/jxvCDRLy9h7V7/TpJ4VUUuFQejoC9STH6K80Z3A5QZfzVbEtC6+Ym67/WzFu65D00aFuOuNllM2r6KRaeHrjzR0DJykIyHto3+WcwFAlPPWxFjOqrtiQX/2O6cG8Mh/5Ocu5s4FtKG6o/LMMRaluQIMoIQW5kf5ptKDBQPkN6wW8nbELV70S8eITbWd566j8mATSBJlov1B22H8JsuINCZX85ReZJBmYnMR7H84O6/h6mibP+PGNjNb8UPJINgXkva+bDfKtt+ZadME0xa/N9b2Q3tmA4XP47pVkt+quNPe6TImpocE5628hH4VU8RkPN8VkIaanRpje/ioz7Bl35kK1uXqRxdkirLDAdoD8RUB46Gq9HPXmsTFRzbZxW6xuXuy2cSxhfSnjow62MveLRhkLlAg2R/K1FGPCP4HYBzoOMAxtptFYhwNh0EK1963FWTliMMHU09IxMxE95py+MZzhalAMRxdGd90A5kVxkoIXe1lNHAbVfRwGoV+wrlVS3MgU+rt7oGGAaXpMjqNMCU6fpUntJGqQSvJFJLm/3xGGEyB0ddh2+gdc+y+ui0oV56cfp5GXKMcYjdIRz/GKlEU05Fo+9bq9O/9XArmWZFTe1us1+HgP5n2/TW7bAS3mwwDRwBDiNqAwdpAbcd9F+Vy50qZP/dnDReDh89Fy6Jj38rSbYBiLO+WMZnAGxNP4Qj84px2oVjX+n+XfA1gRlYxqEHRJfpBTmLdPwmVlzwd8J+PT/Cqt5du+bETUN07ctE2+Z5r/KpLOIqHvtbXuXaBuEpkOHzaqQzRASAAAAZ+Em/7cFgZYAAeYVpjcAAHyBbOKxxGf7AgAAAAAEWVo=')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

