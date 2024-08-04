# 准备工作：
* 账户改为跨币种保证金 (升级至跨币种保证金模式，要求交易账户中权益不低于 10,000.00 USD)

# 策略模块
1. 策略模块中通过ws实时获取当前仓位和资金余额
2. 获取数据处理模块获取实时收益率排名
3. 开仓逻辑：
   1. 按序处理收益率排名中的交易对
   2. 判断数据是否超时（大于制定时间，比如10s)
      1. 超时则跳过
   3. 检查当前是否允许开仓
      1. 策略是否开启
      2. 现货USDT是否充足（balance > per_order_usd)
      3. 仓位是否达到上限
      4. 收益率是否达标
   4. 两腿下单
      1. 简单逻辑均为超价限价单，比如spot，以asks[5]为买价，future 以 bids[5] 为卖价
      2. 复杂逻辑：
       1. 现货maker，等ws成交消息过来后再下单合约taker，价格同上。风险点在于价格滑动过快
          3. 精度处理
       1. 现货和合约的价格精度，根据市场数据来处理
       2. 现货size精度需要根据市场数据来处理
4. 平仓逻辑
   1. 遍历当前持仓，获取对应的收益率，收益率低于平仓阈值的进行平仓处理
   2. 平仓操作亦是两腿下单，同时操作。