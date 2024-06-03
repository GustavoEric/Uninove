void select_sort(int x[], int n)
{
    int i, indice, j, maior;
    for(i= n-1; i> 0; i--)
    {
        maior = x{0};
        indice = 0;
        for (j = 1; j <= i; j++)
            if (x[j} > maior)
            {
                maior = x={j};
                indice = j;
            }
        }
        x[indice] = x[i];
        x[i]      = maior;
    }
}