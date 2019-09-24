<template>
  <v-container class="pa-2" fluid grid-list-md>
    <v-layout column>
      <v-flex v-for="item in items" :key="item.headline" pa-2>
        <ProductItem :headline="item.headline" :title="item.title" :subtitle="item.subtitle" />
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
        headline: "No.1",
        title: "K-means 추천 알고리즘",
        subtitle:
          "k-평균 클러스터링 알고리즘은 클러스터링 방법 중 분할법에 속한다. 분할법은 주어진 데이터를 여러 파티션 (그룹) 으로 나누는 방법이다. 예를 들어 n개의 데이터 오브젝트를 입력받았다고 가정하자. 이 때 분할법은 입력 데이터를 n보다 작거나 같은 k개의 그룹으로 나누는데, 이 때 각 군집은 클러스터를 형성하게 된다. 다시 말해, 데이터를 한 개 이상의 데이터 오브젝트로 구성된 k개의 그룹으로 나누는 것이다. 이 때 그룹을 나누는 과정은 거리 기반의 그룹간 비유사도 (dissimilarity) 와 같은 비용 함수 (cost function) 을 최소화하는 방식으로 이루어지며, 이 과정에서 같은 그룹 내 데이터 오브젝트 끼리의 유사도는 증가하고, 다른 그룹에 있는 데이터 오브젝트와의 유사도는 감소하게 된다.[7] k-평균 알고리즘은 각 그룹의 중심 (centroid)과 그룹 내의 데이터 오브젝트와의 거리의 제곱합을 비용 함수로 정하고, 이 함수값을 최소화하는 방향으로 각 데이터 오브젝트의 소속 그룹을 업데이트 해 줌으로써 클러스터링을 수행하게 된다."
      },
      {
        headline: "No.2",
        title: "EM 추천 알고리즘",
        subtitle:
          "기댓값 최대화 알고리즘은 1977년 아서 뎀스터, 낸 라드와 도널드 루빈에 의해 제시되었다. 하지만 특수한 경우에서의 기댓값 최대화 알고리즘은 이미 몇몇 저자들에 의해 연구되고 있었고, 특히 롤프 선드버그는 페르 마틴-뢰프, 앤더스 마틴-뢰트와 함께 지수족에 한정된 기댓값 최대화 알고리즘에 관한 연구를 한 바 있다. 1977년 뎀스터-라드-루빈 논문은 이 방법을 일반화하여 지수족뿐만 아니라 다양한 확률분포에 한해서도 알고리즘이 수렴함을 밝혔다. 왕립통계협회저널에 게재된 이 논문은 그 혁신성으로 인해 롤프 선드버그를 비롯한 여럿에게 극찬을 받았으며, 기댓값 최대화 알고리즘을 통계분석의 중요한 도구로 자리매김하게 하였다."
      }
    ]
  })
};
</script>