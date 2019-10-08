<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex v-for="item in items" :key="item.id" pa-2>
        <v-card class="mx-auto" max-width="100%" outlined>
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">{{item.title}}</v-list-item-title>
              <div class="overline mb-4">구독자 수: {{item.subscriber}} 명</div>
              <v-list-item-subtitle>{{item.subtitle}}</v-list-item-subtitle>
            </v-list-item-content>

            <v-btn @click="Cancel()" color="red darken-2" class="white--text" v-if="Subscribe(item.id)">구독 취소</v-btn>
            <v-btn @click="Confirm(item.id)" color="red darken-2" class="white--text" v-else>구독</v-btn>
          </v-list-item>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      subscribe: 1,
      items: [
        {
          id: 1,
          title: "KNN 유저 추천",
          subscriber: 3820,
          subtitle:
            "유저가 현재 본 영화를 바탕으로 유저 유사도를 측정하여 평점이 높은 순서로 영화를 추천합니다."
        },
        {
          id: 2,
          title: "KNN 영화 추천",
          subscriber: 1240,
          subtitle:
            "영화를 본 유저를 바탕으로 영화 유사도를 측정하여 평점이 높은 순서로 영화를 추천합니다."
        },
        {
          id: 3,
          title: "MF 영화 추천",
          subscriber: 1200,
          subtitle: "매트릭스 팩토리제이션"
        }
      ]
    };
  },
  methods: {
    Confirm(id) {
      this.subscribe = id;
    },
    Cancel() {
      this.subscribe = 0;
    },
    Subscribe(id){
      if(id == this.subscribe){
        return true;
      }
      return false;
    }
  }
};
</script>