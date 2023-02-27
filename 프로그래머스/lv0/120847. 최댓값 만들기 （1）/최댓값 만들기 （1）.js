function solution(numbers) {
    const max1 = Math.max(...numbers)
    const index1 = numbers.indexOf(max1)
    numbers[index1] = 0
    const max2 = Math.max(...numbers)
    return max1 * max2;
}