import { process } from "process";

export const PROMPTS_API_BASE_URL = process.env.VUE_APP_PROMPTS_API_BASE_URL;
export const PROMPTS_API_LIST_PROMPTS_URL = PROMPTS_API_BASE_URL + "/prompts/";
