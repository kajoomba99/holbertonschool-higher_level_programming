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

	while (temp != NULL)
	{
		while (temp != comp && comp != NULL)
		{
			if (temp->next == comp)
				return (1);
			comp = comp->next;
		}
		temp = temp->next;
		comp = list;
	}

	return (0);
}
