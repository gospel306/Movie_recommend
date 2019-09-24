<template>
  <v-content>
    <Header></Header>
    <Nav></Nav>
    <v-container fluid class="grey lighten-4">
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
</style>
