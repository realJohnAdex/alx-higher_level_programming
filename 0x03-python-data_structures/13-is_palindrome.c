#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr;
	listint_t *slow_ptr, *prev_slow_ptr;
	listint_t *second_half;
	int status = 1;

	if (*head == NULL || (*head)->next == NULL)
		return status;

	fast_ptr = *head;
	slow_ptr = *head;
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		prev_slow_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	if (fast_ptr!= NULL)
	{
		slow_ptr = slow_ptr->next;
	}

	second_half = slow_ptr;
	reverse_list(&second_half);

	prev_slow_ptr->next = NULL;
	status = compare_list(second_half, *head);
	return (status);
}

/**
 * compare_list - checks if a two linked list are the same
 * @a_list: pointer to pointer of first node of listint_t list
 * @b_list: pointer to pointer of first node of listint_t list
 * Return: 0 if false, 1 if tru
 */
int compare_list(listint_t *a_list, listint_t *b_list)
{
	listint_t *a_temp;
	listint_t *b_temp;

	a_temp = a_list;
	b_temp = b_list;
	while(a_temp && b_temp)
	{
		if(a_temp->n == b_temp->n)
		{
			a_temp = a_temp->next;
			b_temp = b_temp->next;
		}
		else
			return 0;
	}
	if (a_temp == NULL && b_temp == NULL)
		return 1;
	return 0;
}

/**
 * reverse_list - reverse a linked list
 * @a_list: pointer to pointer of first node of listint_t list
 * Return: void
 */
void reverse_list(listint_t **a_list)
{
	listint_t *previous, *current, *future;

	current = *a_list;
	previous = NULL;
	while(current != NULL)
	{
		future = current->next;
		current->next = previous;
		previous = current;
		current = future;
	}
	*a_list = previous;
}
