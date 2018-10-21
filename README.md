**Note:** This project is not maintained and the code no longer works due to dependent service changes and the mainter's lack of interest in updating it. I am only uploading it now to add to my portfolio.

**Description:** _CryptoBot_ is a project I created in 2017 during the height of the cryptocurrency craze to analyze crypto prices and and see if such a bot could actually make money. **IT DOES NOT ACTUALLY TRADE**, it only mocks the buy/sell transactions (but using real prices) and keeps track of the current amount of "capital" and "coins".

**How It Works:** The script starts out with 1000 of a coin (whatever coin is configured to be tracked, i.e.: etherium). Every x  number of seconds it gets the current price in BTC of that coin. The algorithm determines if the bot should sell or buy depending on price and amount of capital available. The script prints these transactions out to `CryptoBot.txt` so you can see how much you are making or losing.

The output would look something like this:
```
Initial Price Queue: [0.00196192, 0.00195997, 0.00195997, 0.00195997] 

Time: 2018-01-05 12:20:20
Updated Queue:  [0.00195997, 0.00195997, 0.00195997, 0.00196192]
Capital: 0.0 BTC
Number of Coins: 1000.0
Current price: 0.00196192 BTC

=================================================

Time: 2018-01-05 12:20:51
Updated Queue:  [0.00195997, 0.00195997, 0.00196192, 0.001956]
Capital: 0.0 BTC
Number of Coins: 1000.0
Current price: 0.001956 BTC

=================================================

Time: 2018-01-05 12:27:10
Updated Queue:  [0.00193002, 0.00196977, 0.001959, 0.00191467]

1000.0 of coins sold for 0.00191467
Profit: 1.914670000000000043768877411 BTC


-- Sold coins! --

Capital: 1.914670000000000043768877411 BTC
Number of Coins: 0
Current price: 0.00191467 BTC

=================================================

Time: 2018-01-05 12:27:43
Updated Queue:  [0.00196977, 0.001959, 0.00191467, 0.00191467]
Capital: 1.914670000000000043768877411 BTC
Number of Coins: 0
Current price: 0.00191467 BTC

=================================================

Time: 2018-01-05 12:35:38
Updated Queue:  [0.00193, 0.00191521, 0.00193, 0.001945]

984.4061696658098430821501606 of coins bought for 0.001945


-- Bought coins! --

Capital: 0.0 BTC
Number of Coins: 984.4061696658098430821501606
Current price: 0.001945 BTC

=================================================
```

In case you were wondering, my lack of knowledge about trading algorithms became apparent as I seemed to end up losing money or making minimal gains at best. However, the project itself was a success in that I was able to come to that conclusion without spending a money.
