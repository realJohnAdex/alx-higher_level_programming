#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if listint_t list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *hare;
	listint_t *tortoise;
	int found = 0;

	hare = list;
	tortoise = list;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
		{
			found = 1;
			break;
		}
	}
	return (found);
}
