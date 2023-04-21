<template>
    <button @click="setCookie">{{ buttonText }}</button>
</template>

<script>
import { PROMTPS_OPENAI_API_KEY_COOKIE_NAME } from '@/settings';

const NOT_AUTHENTICATED_BUTTON_TEXT = "Authenticate 🔓";
const AUTHENTICATED_BUTTON_TEXT = "Authenticated 🔐";


export default {
    data() {
        return {
            'openai_api_key': null
        }
    },
    mounted() {
        this.openai_api_key = this.getOpenAIApiKeyCookie();
    },
    methods: {
        getOpenAIApiKeyCookie() {
            return this.$cookies.get(PROMTPS_OPENAI_API_KEY_COOKIE_NAME);
        },
        setCookie(){
            if (this.$cookies.isKey(PROMTPS_OPENAI_API_KEY_COOKIE_NAME)) {
                this.$cookies.remove(PROMTPS_OPENAI_API_KEY_COOKIE_NAME);
                this.openai_api_key = null;
            }
            else {
                this.$cookies.set(PROMTPS_OPENAI_API_KEY_COOKIE_NAME, "key123");
                this.openai_api_key = "key123";
            }
        }
    },
    computed: {
        buttonText() {
            return this.openai_api_key === null ? AUTHENTICATED_BUTTON_TEXT : NOT_AUTHENTICATED_BUTTON_TEXT;
        },
    }
}
</script>