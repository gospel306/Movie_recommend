<template>
  <v-navigation-drawer
    v-model="drawer"
    app
    clipped
    src="http://mblogthumb1.phinf.naver.net/MjAxNzAyMjFfMjc2/MDAxNDg3Njg4OTUxOTk4.9xNsOsXbtth8enRO3Lodh3zNDyvdIcjO76diXPvfSlAg.FUQuMQZ0TFI6hjSfvaH6piHXcYYlkT7nsZbrwzLwdE0g.JPEG.younilog/%EB%B8%94%EB%9E%99%EB%B0%B0%EA%B2%BD%ED%99%94%EB%A9%B4_%EA%B2%80%EC%A0%95%EB%B0%B0%EA%B2%BD%ED%99%94%EB%A9%B4_%EC%8A%A4%EB%A7%88%ED%8A%B8%ED%8F%B0%EB%B0%B0%EA%B2%BD%ED%99%94%EB%A9%B4_%EA%B0%A4%EB%9F%AD%EC%8B%9C%EB%B0%B0%EA%B2%BD%ED%99%94%EB%A9%B4_.jpg?type=w800"
  >
    <v-list dense>
      <v-list-item-title class="title white--text">유저</v-list-item-title>
      <v-divider></v-divider>
      <template v-for="(choice, i) in users">
        <v-list-item
          :key="i"
          @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
            }"
        >
          <v-list-item-action>
            <v-icon color="white">{{ choice.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="subtitle-2 font-weight-bold white--text">{{ choice.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>

      <v-list-item-title class="title white--text">영화</v-list-item-title>
      <v-divider></v-divider>
      <template v-for="(choice, i) in movies">
        <v-list-item
          :key="i"
          @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
            }"
        >
          <v-list-item-action>
            <v-icon color="white">{{ choice.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="subtitle-2 font-weight-bold white--text">{{ choice.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "Nav",
  components: {},
  data() {
    return {
      drawer: null,
      users: [
        {
          icon: "mdi-account",
          text: "유저 정보",
          path: "userlist"
        }
      ],
      movies: [
        {
          icon: "mdi-movie",
          text: "영화 검색",
          path: "search"
        },
        {
          icon: "mdi-movie",
          text: "추천 영화",
          path: "best"
        },
        {
          icon: "mdi-movie",
          text: "상품 소개",
          path: "productlist"
        }
      ]
    };
  },
  methods: {
    goTo(path) {
      this.$router.push(path);
    }
  }
};
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none;
}
</style>

