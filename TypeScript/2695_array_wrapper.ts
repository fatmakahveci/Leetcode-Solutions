class ArrayWrapper {
    private nums: number

    constructor(nums: number[]) {
        this.nums = nums;
    }

    valueOf() {
        return this.nums.reduce((sum,val) => sum + val, 0);
    }

    toString() {
        return JSON.stringify(this.nums);
    }
};
