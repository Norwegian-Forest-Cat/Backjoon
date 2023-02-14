function solution(n) {
    if (n === 1){   // 예외처리
        return 0
    }
    
    let array = []
    for (let i = 1; i <= n; i++) {
        i % 2 === 0 ? array.push(i) : null
    }
    return array.reduce((a, b) => a + b)
}