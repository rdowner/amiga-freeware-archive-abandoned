<template>
    <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <DiskInfo v-bind:disk="diskdetail"></DiskInfo>
    </div>
</template>

<script>
    import DiskInfo from './components/DiskInfo.vue'
    import axios from 'axios'

    export default {
        name: 'app',
        components: {
            DiskInfo
        },
        data: function(){
            return {
                diskdetail: {}
            };
        },
        created: function(){
            axios.get('/libraries/fish/disks/573')
                .then(response => {
                    this.diskdetail = response.data;
                });
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
