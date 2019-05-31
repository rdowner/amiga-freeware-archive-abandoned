<template>
    <div>
        <h1>Here's a disk.</h1>
        <DiskInfo v-bind:disk="diskdetail"></DiskInfo>
    </div>
</template>

<script>
    import DiskInfo from './DiskInfo.vue'
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
        created () {
            this.fetchData()
        },
        watch: {
            '$route': 'fetchData'
        },
        methods: {
            fetchData() {
                axios.get('/libraries/'+this.$route.params.library+'/disks/'+this.$route.params.disk)
                    .then(response => {
                        this.diskdetail = response.data;
                    });
            }
        }
    }
</script>

<style scoped>
</style>
