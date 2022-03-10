<template>
  <div class="home">
    <Mainblock />
    <AboutUs />
    <ThirdBlock />
    <FourthBlock />
    <HaveIdea />
    <Partners />
  </div>
</template>

<script>
import Mainblock from "@/components/Main_block.vue"
import AboutUs from "@/components/AboutUs.vue"
import ThirdBlock from "@/components/ThirdBlock.vue"
import FourthBlock from "@/components/FourthBlock.vue"
import HaveIdea from "@/components/HaveIdea.vue"
import Partners from "@/views/Partners.vue"

export default {
  name: 'Home',
  components:{
    Mainblock,
    AboutUs,
    ThirdBlock,
    FourthBlock,
    HaveIdea,
    Partners
  }
}
</script>
