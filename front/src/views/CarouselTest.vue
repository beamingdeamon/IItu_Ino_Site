<template>
    <Carousel
        :ItemData = "partners"
        :interval = "0"/>
</template>

<script>
import axios from 'axios'
import Carousel from './Carousel.vue'
export default {
    data(){
        return{
            partners: new Array()
        }
    },
    components: {
        Carousel
    },
    mounted(){
        axios.get('http://localhost:8000/api/getpartners/')
        .then( response => {this.partners = response.data} )
        .catch(function (error) {
        console.log(error);
        })
    }
}
</script>

<style lang="sass" scoped>

</style>