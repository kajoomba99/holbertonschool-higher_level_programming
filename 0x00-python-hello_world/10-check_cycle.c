#include "lists.h"
/**
 * check_cycle - check_cycle
 * @list: list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *comp = list;

	if (list == NULL)
		return (0);

	while (temp != NULL && comp != NULL && temp->next != NULL)
	{
		temp = temp->next->next;
		comp = comp->next;
		if (temp == comp)
			return (1);
	}

	return (0);
}
