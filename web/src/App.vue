<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <ProductInfo v-bind:infos="pi"></ProductInfo>
    </div>
</template>

<script>
    import ProductInfo from './components/ProductInfo.vue'

    export default {
        name: 'app',
        components: {
            ProductInfo
        },
        data: function(){
            return {
                pi: {"name": "foo", "thing": "bar"}
            };
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
