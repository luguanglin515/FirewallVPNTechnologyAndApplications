#define _WINSOCK_DEPRECATED_NO_WARNINGS // 禁用旧函数警告
#include <stdio.h>
#include <winsock2.h>

// 告诉编译器链接 Windows 网络库
#pragma comment(lib, "ws2_32.lib")

int main()
{
    // --- Windows 额外步骤：初始化网络库 ---
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("Winsock 初始化失败\n");
        return 1;
    }

    // --- 核心逻辑（与实验要求一致） ---
    struct hostent* host = gethostbyname("www.yxnu.edu.cn");
    if (!host)
    {
        printf("查询失败，错误代码: %d\n", WSAGetLastError());
        WSACleanup();
        return 1;
    }

    // 打印 IP 地址
    printf("IP: %s\n", inet_ntoa(*(struct in_addr*)host->h_addr));

    // --- Windows 额外步骤：清理网络库 ---
    WSACleanup();
    return 0;
}