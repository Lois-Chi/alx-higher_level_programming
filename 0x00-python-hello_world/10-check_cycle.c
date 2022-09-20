#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to start of linked list
 * Return: 0 or 1 based on a condition
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (list == NULL)
		return (0);
	while (a != NULL && b != NULL && b->next != NULL)
	{
		tortoise = tortoise->next;
		b = b->next->next;
		if (a == b)
			return (1);
	}
	return (0);
}
