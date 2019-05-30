<template>
    <div>
        <h1>{{ disk.name }}</h1>
        <p>#{{ disk.volume_number }}</p>
        <p>{{ disk.alternative_name }}</p>
        <p>{{ disk.description }}</p>
        <div v-for="artifact of disk.artifacts" v-bind:key="artifact.artifact_id">
            <ProductInfo v-bind:product="artifact"></ProductInfo>
        </div>
    </div>
</template>

<script>
    import ProductInfo from './ProductInfo.vue'

    export default {
        name: 'DiskInfo',
        components: {
            ProductInfo
        },
        props: {
            disk: Object
        }
    }
</script>

<style scoped>
</style>