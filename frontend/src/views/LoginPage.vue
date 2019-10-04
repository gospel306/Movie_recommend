<template>
    <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm8 lg4 md5>
          <v-card class="login-card">
            <v-card-title>
              <span class="headline">Login</span>
            </v-card-title>
            <v-spacer/>
            <v-card-text>
              <v-layout
                row
                fill-height
                justify-center
                align-center
                v-if="loading"
              >
                <v-progress-circular
                  :size="50"
                  color="primary"
                  indeterminate
                />
              </v-layout>


              <v-form v-else ref="form" v-model="valid" lazy-validation>
                <v-container>
                  <v-text-field
                    v-model="credentials.username"
                    :counter="70"
                    label="email address"
                    maxlength="70"
                    required
                  />
                  <v-text-field
                    type="password"
                    v-model="credentials.password"
                    :counter="20"
                    label="password"
                    maxlength="20"
                    required
                  />
                </v-container>
                <v-btn class="black white--text" :disabled="!valid" @click="login">Login</v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios';
import router from '../router';

export default {
    name: 'Login',
    data: () => ({
        credentials: {},
        valid:true,
        loading:false
    }),
    methods: {
        login() {
          // checking if the input is valid
            if (this.$refs.form.validate()) {
              this.loading = true;
              axios.post('http://localhost:8000/api/login/', this.credentials).then(res => {
                this.$store.state.login = true;
                this.$session.start();
                this.$session.set('token', res.data.token);
                this.$session.set('id', this.credentials.username);
                alert("로그인 성공");
                router.push('/search');
                
                // eslint-disable-next-line
              }).catch(e => {
                this.loading = false;
              });
            }
        }
    }
}
</script>
