//堆排序
#include<stdio.h>

void swap(int *a,int *b);
void heapify(int arr[],int n,int i);
void heapSort(int arr[],int n);

int main()
{
    int arr[] = {4, 10, 3, 5, 1};  // 测试数据
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("原始数组: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");

    heapSort(arr, n);

    printf("排序后数组: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}

void swap(int *a,int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(int arr[],int n,int i) //对前i个元素建堆
{

    int largest = i; //当前节点，视为最大元素
    int left = 2*i+1; //左节点
    int right = 2*i+2; //右节点
    
    if(left<n && arr[left]>arr[largest])
    {
        largest = left;
    }
    if(right<n && arr[right]>arr[largest])
    {
        largest = right;
    }
    if(largest != i)
    {
        swap(&arr[i],&arr[largest]); //交换当前节点与最大元素节点
        heapify(arr,n,largest); //继续递归
    }
}

void heapSort(int arr[],int n)
{
    //从最后一个非叶子节点开始建堆
    for(int i=n/2-1;i>=0;i--)
    {
        heapify(arr,n,i);
    }
    for(int i=n-1;i>0;i--)
    {
        swap(&arr[0],&arr[i]); //取出堆顶元素
        heapify(arr,i,0); 
    }
}