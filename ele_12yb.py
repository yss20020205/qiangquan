
"""
抢12
卡密变量 lqkm
账号变量 elmqqck
推送变量  lp , id
lp为 wxpusher 账号令牌
id为 wxpusher id
 * cron: 55 53 9 * * *

令牌和id获取方式
打开后台  
https://wxpusher.zjiecode.com/admin/main
应用管理-appToken 就是令牌 
主题管理-TopicId 就是id


内置定时 09:59:59
脚本定时 55 50 9 * * * 
默认一个账号抢劵次数20次 200毫秒
暂不支持修改

"""
const $ = new Env('饿了么12异步抢券--嘎嘎好使');

import lzma, base64
exec(lzma.decompress(base64.b64decode('/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4BulCstdADSbSme4Ujxz9PV7sB8UcIoUWuZs9sNkRf/1SgcKaWzYgR5aDpehK9tg771pjq1DB4u5hmBtb6P9XcNvmGU7fI7McDb7joxfbGElqqskFy0CCY2HjNniiSbjCzHe0tk77nx6dB8SHC4xKuPtja6rN7X2tBJHlZ0+Cnv3NgebzooreAvoAeT4+SCbwaf9L98IilSHYmh9oCUzNNB2FXz4tm99Aj1+E7wYsv2p/TDTeK62AgUfno7DA9L1py5H8Wv09q/xzxitEwoE6a+bNPHkhMJz2N/yk7gR/WCpp+JRVp+Fo7cM7HXUS3qg+Uc4WZ2bDGFXIjvOcb6QAqr+Zfmw6ZxnOZUpzI0y4SPSzYCnnBUKdOtF2sq9Aw9E2u+d8VftVk5cSKrPwg6MdkhT1w951xgo4qjj61Kgk1a39AVKMofX2kyxk421ONLjT6j60idko5mkj5Hsu5bHGSCvFe6pc6i435Vr8kM2mic3s7o+ula8oxAHDHYdd50eKVYUZhoPqOxRuIvIPWdbbldlA0qtq7JpQMOEvrYG7k/KXS7/4btSQW4Yfdil26qACUdOcfK+uK2ZuYQCuCp87dSSqP8OtwC/igKz1YrwRzV64JkIXy/ZVstf4DtKzMw6L9Snnfiu7gXyiz7VT53upGCx7LGqIL8mAtVQUjCbK55YFfZqtFer9hz/WlXOW/BynVgbCHpkBd/gC8h015YUmycUpW00mQzH8jaxy6ebawCZUrXQFdLraGI2jnacFdags1HFUs30D178ro8qI90OpGQePK+zp9Fl9UXinOewCgjTaq/xmKiFNklIwakz+uTUhEvrdqYDEWkDNcTmEelBDBbfl1SEHUs5zF68g8IpgoxkQdEBD1yxsnNh8Dw4BMSqIjR0MObMpwQDZ3NdstQYoaHwic1QYRUDoEshLWXI6qA8Ygwhmej5yTux7crWDbXazxLE1Z1LH6mujWuhVpnLJYmDVeXtpjejD0yFh3VHvzRoYPyifSg17sLWG85YHjLTvXTXVD9sQtIufb9ZxzyxODP2RFQKPxK+eBrQzlE0nRvs5+bmhTWw3LcUklk0/ZcX9t9GIIdyMsdS94C3jhQXEuPYxQoXDY62BlF0HwhxXfnp6JkFGYJIh6I86hnRPjLVzQiBaAyG7DRD4AvaXHAdkPUclXHn1byLfQombqN9Iunny8xMmcVX1XSJD0eIaL2JnH/H3TU4rHbQdjG/ZamO/0ZNzom0Ozg34x+Umhlpcs1X01GieGvEhtovLoTIIy3/yL1OM3KxdsW4KWX05JBMm/gHx2g++FV+L0/unwGPkZS94gtXUlEm6QH/MXEHbvkSX/B5utHOkfWYVQh7ay+16hlPTMa7d8UV7VL1hVgjApPzLuEE2MsNu4lnH0Ko/dY8tuUk0DAG3bIX3pAqyUYhrqbp/KzopJH2jZAcZgcHmtbw7RM36VCq6WA4JF8azH0d39ns3+9klQKZIaYmtaIxOiVriwjr+PK+ZVZDJEitmCSgAObmYbo9ivOf960ZjWi2m16L/NXC3+5D1X6wngV5C/6f9wNbRSHWL9GKoQoKJV+JPNaJ7zouZny1GfZvHJLx1yIeyQ5utAXhMKO+a02JnEZ5BWCYh+80MWM4/qGQgsJ+1dJ4GiZy+Bpa7qsYihXiJJdMRbmZP3FW44pp+7xDAsRdTDrYBdghAqHNkMj+peftKfq+sN1lNcIdU1Yr9FBgA/jR2cl470j0XGpD50clEYzkdnZd5QYP2x1ROn5m7fGXlOBN3SlkA+f4KPu6fCpyPBHj1Jup4KkCWKuh/uP4ka6HhLZI4phsSM23M+LLAh+NI+jkaurzJeFKvwkwChtv/Vj6vgLxVAdI/tAF7lTXEYkmssfqTrr3AX1/ppSvRznrCFSDLrUs4zeaNB+A7yiCIEQAXXO1B8fyCAzq41qYHkEyMKaKXuL1aB9ODwx2M+3VvzAKz5aDEqKYJ/bFAxNoKZhlcC6aWet+4tO7qKYlAq/Tj6eD15Kfin00brVGDoPZQYgh1eXS4E//sbIF1rt7x4Jl7ZG2xaet0uII+Lf3RKqHkBQtgoA1B5Z7S9SzOfci/pJ8DYnFF8TQcvYy9e5Fna55FRu3P71rrsON9s3wL/9N1wTBOf2AkuGJl1BZwLU60gP5cxEIAJM1oYM+ikHybapUyYFldGXX+XAKnbrotIO8jXEsWT6igARqPElyKwShZsK5xQXQNw3k4wdlq2l/VPDDTGLSaevaBuLH776KwjmUQKQ1uxmNC6FqtQqb6UtdmIqWhJZSpuqwUIE7EfvGMhm4OifvOQDh/78wJk2BUanlUU3UUVBZ07meezUO/EoTHia+hmTPfIeCqkweCO6EbYuvtOZHOPZHldN0c1CQWneHTEok13QnRMxCbgtF7bc1raGxytPq/c4i/Jftc6A+QjOnznQJd3OLGBg9zxtGMyADinYxcM2c4/lNKf0IdtjU1f8JR+IpXczQKp65IR9NT+hY/JrEolbmsu57U0bVgju0+16kQFmLdoRVIer5uQ48ys5E4NzaYs2Djuw216XWaFsd03TVfH3rLVJTYClz2CsH+toMyGWXKM0R+uhIr0Xz7eYx2PD726Fap9a2Qb9S2rt6OADlOEWrUFjFTtUCI6hflmR0SvBrsBGNwG3zVWYU/e3yOvU3ijbJS2UKIDDDgw1mgV+opdx596atDnuni/JXX/Ra9AsymFnC1CiZ5arS8TxXixi4IcrVEQx5M/FfnalclpqNgP+1RzD/yRVgrKUEcXx3l0Xc8iLK1ISBby8AoZIpyKyYg7KYDQy1O5gYuBY1URhaOOtgkkfK4pLUhaEYHQlRLTL2CJKGaNunr5gp+HWGZZFYTte8GRgFWQ6RIUAJXW+UTsc6V/F/Uw54umL5M+ib6YZfjuQlAaM/+gKPP1k+ujPzSp6c+yu4ZjI2xRJDFa2cFYOZEmOiRiZMf/cphBJdYKiGVxDKL5Su5ifOhK8nJSA3AyoEGjc5eRRNkVHhlX6vD9VV//O6N8lF0Re54kxTPNj/JEnZn1I5S/vl61p+Z7pz3woZOj5SaVgKoqLbpAOkfUUPHY0k01PdwIa+YH9A1ABBofkh/fezR62tEPwBKfkoewqaan6Q6hvA35YF85NK2y7+52P6H0PCOaWRnm6U9JKWHxCi6tBJ/S84H0mAh2AfJCPEf5kwDheNkXiEP1VeY7xM4EgxB/1U7J1hfEUODOWx8iiYg+NpIaIJKdYRotrnMt4k3zngGDB/Sqbcob6LOglmyVjjsNpT2UkR2Qy0aQcZU0VwUo4Mcw09uiJ+Mu85hPf7HjaHaeTnsxHuH0x46mBiZqCNao+yJndkyHKlwWQaojAfRcPkU580AMHlubXPr7mvY+a3S9MAC0stYyTFSPSFHWPdGyfKhKETLqpN2nIxMXxiG7wB4Y3VQdhJOpG85rfcdBWrheFh5ua2cX7u8u812b1a6fRrO221l1QC12RR/sPQg+vf0sEbsyzthdKLL4lms8aYNXJbmkXW6tkDYG9ck5wKqIR9N9yvX0O4vg+iNjVs4ubEpdHcciWujnPWX/0K1aFhXMfWPqs+WfVEpki6WYLl0oat7cE40GqYKfkbw+EEJariki5iF6pmQb9FToakkI1ZsjpybHe6HycKgt3NQsfnGnLutI5wQBpK4R3vBppYEmRz5XfEkQAArX2jAEe1mYEAAecVpjcAANlSMCmxxGf7AgAAAAAEWVo=')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

