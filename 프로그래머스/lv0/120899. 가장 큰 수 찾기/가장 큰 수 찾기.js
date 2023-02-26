function solution(array) {
    let answer = []
    answer.push(Math.max(...array))
    for (let i = 0; i < array.length; i++) {
        if (array[i] === answer[0]) {
            answer.push(i)
            break
        }
    }
    return answer
}