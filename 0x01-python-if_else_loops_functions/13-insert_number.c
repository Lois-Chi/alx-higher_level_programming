#include "lists.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - insert a new node to a sorted list
 * @head: head of linked list inserted
 * @number: number to insert
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *New;
	listint_t *actual;

	New = malloc(sizeof(listint_t));

	if (New == NULL)
		return (NULL);

	New->n = number;
	if (*head == NULL)
	{
		*head = New;

		New->next = NULL;
		return (New);
	}
	actual = *head;
	while (actual)
	{
		if (number <= actual->n)
		{
			New->next = actual;
			*head = New;
			return (New);
		}
		if ((number >= actual->n) && (actual->next == NULL))
		{
			New->next = NULL;
			actual->next = New;
			return (New);
		}
		if ((number >= actual->n) && (number <= actual->next->n))
		{
			New->next = actual->next;
			actual->next = New;
			return (New);
		}
		actual = actual->next;
	}
	return (NULL);
}
