function solution(array, n) {
    let answer = 0
    for (let i = 0; i < array.length; i++) {
        if (n === array[i]) {
            answer++
        }
    }
    return answer;
}