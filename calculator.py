from datetime import date

def build_row(json_data: dict) -> dict:
    record = json_data["data"]["trans_record"]

    register_amount = int(record["register_amount"])
    win_lose_amount = float(record["win_lose_amount"])
    deposit_count = int(record["deposit_count"])
    deposit_amount = float(record["deposit_amount"])
    first_deposit_count = int(record["first_deposit_count"])
    first_deposit_amount = float(record["first_deposit_amount"])
    withdrawal_count = int(record["withdrawal_count"])
    withdrawal_amount = float(record["withdrawal_amount"])
    withdrawal_fee = float(record["withdrawal_fee"])
    bet_count = int(record["bet_count"])
    bet_amount = float(record["bet_amount"])
    bet_user_count = int(record["bet_user_count"])
    bet_fee = float(record["bet_fee"])
    manual_adjust_amount = float(record["manual_adjust_amount"])
    rebate_amount = float(record["rebate_amount"])
    promotion_amount = float(record["promotion_amount"])
    agent_bonus_amount = float(record["agent_bonus_amount"])

    diff_dep_withdraw = deposit_amount - withdrawal_amount
    exchange_rate = 2.0
    diff_dep_withdraw_cny = diff_dep_withdraw / exchange_rate
    bet_amount_cny = bet_amount / exchange_rate

    platform_profit = (
        win_lose_amount
        + bet_fee
        + withdrawal_fee
        - rebate_amount
        - promotion_amount
        - agent_bonus_amount
        + manual_adjust_amount
    )
    platform_profit_cny = platform_profit / exchange_rate

    today = date.today()

    return {
        "日期": today.strftime("%Y-%m-%d"),
        "新注册人数": register_amount,
        "会员总数": 0,
        "池内总金额": 0,
        "池内总金额(CNY)": 0,
        "游戏输赢": win_lose_amount,
        "充值总金额": deposit_amount,
        "充值人数": deposit_count,
        "首充总人数": first_deposit_count,
        "提现总金额": withdrawal_amount,
        "提现总人数": withdrawal_count,
        "提现手续费": withdrawal_fee,
        "充提差": diff_dep_withdraw,
        "充提差(CNY)": diff_dep_withdraw_cny,
        "投注总额": bet_amount,
        "注单总数": bet_count,
        "游戏手续费": bet_fee,
        "投注人数": bet_user_count,
        "投注总额(CNY)": bet_amount_cny,
        "人工调整": manual_adjust_amount,
        "VIP返水": rebate_amount,
        "优惠": promotion_amount,
        "代理返佣": agent_bonus_amount,
        "奖金派发总金额": 0,
        "平台盈利(平台角度)": platform_profit,
        "平台盈利(CNY)": platform_profit_cny,
        "本日汇率": exchange_rate,
        "年份": today.year,
        "月份": today.month,
    }
