<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex v-for="item in items" :key="item.id" pa-2>
        <v-card class="mx-auto" max-width="100%" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">{{item.title}}</v-list-item-title>
              <div class="overline mb-4">구독자 수: {{item.subscriber}}</div>
              <v-list-item-subtitle>{{item.subtitle}}</v-list-item-subtitle>
            </v-list-item-content>

            <v-btn
              @click="Cancel()"
              color="red darken-2"
              class="white--text"
              v-if="Subscribe(item.id)"
            >구독 취소</v-btn>
            <v-btn @click="Confirm(item.id)" color="red darken-2" class="white--text" v-else>구독</v-btn>
          </v-list-item>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      subscribe: 1,
      cluster: {},
      items: [
        {
          id: "KNN_user",
          title: "KNN 유저 추천",
          subscriber: "추후 업데이트 예정",
          subtitle:
            "유저가 현재 본 영화를 바탕으로 유저 유사도를 측정하여 평점이 높은 순서로 영화를 추천합니다."
        },
        {
          id: "KNN_movie",
          title: "KNN 영화 추천",
          subscriber: "추후 업데이트 예정",
          subtitle:
            "영화를 본 유저를 바탕으로 영화 유사도를 측정하여 평점이 높은 순서로 영화를 추천합니다."
        },
        {
          id: "MF",
          title: "MF 영화 추천",
          subscriber: "추후 업데이트 예정",
          subtitle: "매트릭스 팩토리제이션"
        }
      ]
    };
  },
  mounted() {
    this.getUserSubscribe();
  },
  methods: {
    nowDate() {
      var now = new Date();
      var year = now.getFullYear();
      var month = now.getMonth() + 1;
      var day = now.getDate();
      return year + "-" + month + "-" + day;
    },
    Confirm(id) {
      axios
        .put(
          this.$store.state.server +
            "/api/subscribe/?id=" +
            this.$session.get("id") +
            "&cluster=" +
            id
        )
        .then(() => {
          this.cluster.cluster = id;
          this.$session.set("cluster", this.cluster.cluster);
        });
    },
    Cancel() {
      axios
        .put(
          this.$store.state.server +
            "/api/subscribe/?id=" +
            this.$session.get("id") +
            "&cluster="
        )
        .then(() => {
          this.cluster.cluster = "";
          this.$session.set("cluster", this.cluster.cluster);
        });
    },
    Subscribe(id) {
      if (id === this.cluster.cluster) {
        return true;
      }
      return false;
    },
    getUserSubscribe() {
      axios
        .get(
          this.$store.state.server +
            "/api/subscribe/?id=" +
            this.$session.get("id")
        )
        .then(res => {
          this.cluster = res.data[0];
          this.$session.set("cluster", this.cluster.cluster);
        });
    }
  }
};
</script>