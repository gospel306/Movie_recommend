<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex v-for="item in items" :key="item.id" pa-2>
        <ProductItem :subscriber="item.subscriber" :title="item.title" :subtitle="item.subtitle" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ProductItem from "@/components/product/ProductItem";
export default {
  components: {
    ProductItem
  },
  props: {
    ProductItems: {
      type: Array,
      default: () => new Array()
    }
  },
  data: () => ({
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
        subtitle:
          "매트릭스 팩토리제이션"
      }
    ]
  })
};
</script>