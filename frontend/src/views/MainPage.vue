<template>
  <v-content>
    <Header></Header>
    <Nav></Nav>
    <v-container fluid class="background">
      <router-view></router-view>
    </v-container>
  </v-content>
</template>

<script>
import Header from "@/components/common/Header";
import Nav from "@/components/common/Nav";

export default {
  name: "mainpage",
  data() {
    return {};
  },
  components: {
    Header,
    Nav
  },
  mounted() {},
  methods: {}
};
</script>

<style>
/* .background{
  background: url("http://image.downloadwap.co.uk/wallpapers/p2ls/new/38/wallp_hVnXsXu8uw.jpg");
} */
</style>

