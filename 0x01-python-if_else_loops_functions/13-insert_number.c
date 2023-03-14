#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head of list
 * @number: the number to be inserted
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *previous;
	listint_t *new_node, *temp;

	current = *head;
	previous = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		/* if the list is empty 
		insert new_node */
		*head = new_node;
		return (new_node);
	}
	else if (new_node->n <= (*head)->n)
	{
		/* if the new_node->n is less then first element 
		insert at beginning of list */
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	else
	{
		/* traverse the list 
		if the current->n is greater than new_node->n 
		insert before current node */
		while (current->next != NULL)
		{
			previous = current;
			current = current->next;
			if (current->n >= new_node->n)
			{
				temp = previous->next;
				previous->next = new_node;
				new_node->next = temp;
				return (new_node);
			}
		}
		/* if new_node->n is greater the last node 
		insert after the last */
		temp = current->next;
		current->next = new_node;
		new_node->next = temp;
		return (new_node);
	}
	return NULL;
}
