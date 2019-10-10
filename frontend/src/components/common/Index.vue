<template>
    <v-container>
      <v-layout column align-center>        
        <v-flex sm4>
          <v-img class="intro"
            src="@/images/intro.gif" 
            width="400"
            height="166"
          ></v-img>
        </v-flex>
        <v-flex class="sear">
          <v-layout text-sm-right >
            <v-flex class="pa-1">
              <v-icon large color="black">mdi-magnify</v-icon>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex class="str">
          <h1>이 곳은 빅데이터 기반의 <span class="rd">영화 추천 사이트</span>입니다.</h1>

        </v-flex>
      </v-layout>
    </v-container>
</template>


<script>
export default {
  name: "index",
  data: () => ({

  }),
  methods: {
  },
};
</script>

<style>
.rd{
  color:#d32f2f ;
  font-size:40px;

  }
.intro{
  border-width: 1px;
  border-style: solid;
  border-color: white;
  border-radius: 15px;
  filter: grayscale(100%);
}
.sear{
  border-width: 3px 8px 10px 3px;
  border-style: solid;
  border-color: black;
  margin-top: 60px;
  border-radius: 15px 15px 0px 15px; 

  width: 400px;
  height: 60px;  
}
.str{
  border-width: 0px 0px 4px 0px;
  border-style: solid;
  border-color: black;
  margin-top: 60px;
}
</style>

