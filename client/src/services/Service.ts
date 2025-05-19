import { API_URL } from "@/consts"
import axios, { type AxiosInstance, type AxiosResponse } from "axios"

export class Service<T> {
    instance: AxiosInstance
    constructor(url: string) {
        this.instance = axios.create({
            baseURL: API_URL + url,
            headers: { "Content-Type": "application/json" }
        })
    }

    async GET(url?: string): Promise<AxiosResponse<T>> {
        return await this.instance.get(url || '/')
    }
    async POST(data: T, url?: string): Promise<AxiosResponse<T>> {
        return await this.instance.post(url || '/', data)
    }
    async PATCH(url: string, data: T): Promise<AxiosResponse<T>> {
        return await this.instance.patch(url, data)
    }
    async DELETE(url: string, data: T): Promise<AxiosResponse<T>> {
        return await this.instance.patch(url, data)
    }
}