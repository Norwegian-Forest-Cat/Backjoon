function solution(money) {
    const cup = parseInt(money / 5500)
    return [cup, money - 5500 * cup]
}