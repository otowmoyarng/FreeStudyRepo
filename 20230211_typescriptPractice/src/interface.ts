interface IArray {
    [index: number]: string;
}
interface IReadonly {
    readonly x: number;
    readonly y: number;
}
interface ISample2 {
    name: string;
    age: number;
    tel?: string;
}
interface ISample1 {
    methodHasReturn(arg: string): string;
    methodNoReturn(arg: string): void;
    field1: ISample2;
    field2: IReadonly;
    field3: IArray;
}

export default function interfaceSample(): void {
    const data1: ISample2 = {
        name: "taro",
        age: 10
    };
    const data2: IReadonly = {
        x:1,
        y:2
    };
    const array: string[] = ["hoge","fuga"];
    const sample: ISample1 = {
        methodHasReturn(arg: string) {
            return arg + arg;
        },
        methodNoReturn(arg: string) {
            return console.log('arg', arg);
        },
        field1: data1,
        field2: data2,
        field3: array
    };
    console.log('sample', sample);
    console.log('sample.methodHasReturn()', sample.methodHasReturn("hoge"));
    console.log('sample.methodNoReturn()');
    sample.methodNoReturn("hoge");
    console.log('sample.field1', sample.field1);
    console.log('sample.field2', sample.field2);
    console.log('sample.field3', sample.field3);
    for(let index: number = 0; index < array.length; index++) {
        console.log(`sample.field3[${index}] = ${sample.field3[index]}`);
    }
}