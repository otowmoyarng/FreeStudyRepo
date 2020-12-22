var app1 = new Vue({
    el: '#app1',
    data: {
        message: 'Hello Vue.js!',
        list: ['りんご', 'ばなな', 'いちご'],
        show: true
    },
    methods: {
        handleClick: function(event) {
            alert(event.target)
        }
    }
})

var app2 = new Vue({
    el: '#app2',
    data: {
        message: {
            value: 'Hello Vue.js!'
        },
        // 配列データ 3 と 4 で使用
        list: ['りんご', 'ばなな', 'いちご'],
        // 別のデータを使用してlistから取り出す要素を動的に 4 で使用
        num: 1,
        count: 0,
        isChild: false,
        isActive: true,
        textColor: 'red',
        bgColor: 'lightgray',
        radius: 50,
        list2: [
            { id: 1, name: 'スライム', hp: 100 },
            { id: 2, name: 'ゴブリン', hp: 200 },
            { id: 3, name: 'ドラゴン', hp: 500 }
        ]
    },
    methods: {
        increment: function() {
            this.count += 1
        }
    }
})